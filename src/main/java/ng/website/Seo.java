package ng.website;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

/**
 * What search engines and link previews see: each page's title, description and canonical URL, structured data,
 * the sitemap, robots.txt and the web app manifest
 */

public class Seo {

	public static final String BASE_URL = "https://www.engifer.com";

	public static final String SITE_NAME = "glytta";

	public static final String SITE_DESCRIPTION = "glytta is an open source, component-based Java web framework: HTML templates paired with Java classes, stateful component actions, and deployment alongside WebObjects apps.";

	private static final String REPOSITORY_URL = "https://github.com/ngobjects/ng-objects";

	/**
	 * Descriptions longer than this get cut short in search results
	 */
	private static final int DESCRIPTION_MAX_LENGTH = 160;

	/**
	 * A page's metadata
	 *
	 * @param type The Open Graph type: "website" or "article"
	 * @param indexable false for pages search engines shouldn't list, like search results
	 */
	public record Meta( String title, String description, String type, boolean indexable ) {

		/**
		 * @return The same metadata, naming the site siteName instead (for the engifer look, see Theme)
		 */
		public Meta withSiteName( final String siteName ) {
			return new Meta( title.replace( SITE_NAME, siteName ), description.replace( SITE_NAME, siteName ), type, indexable );
		}
	}

	/**
	 * @return The metadata for the page at the given request URI
	 */
	public static Meta meta( final String uri ) {
		final String path = path( uri );

		if( path.equals( "/" ) ) {
			return new Meta( SITE_NAME + ": a Java web framework", SITE_DESCRIPTION, "website", true );
		}

		for( final Page page : Page.allPages() ) {
			if( page.url().equals( path ) ) {
				final String description = page.description() != null ? page.description() : SITE_DESCRIPTION;
				return new Meta( page.name() + " · " + SITE_NAME, description, "article", true );
			}
		}

		for( final BlogEntry entry : BlogEntry.allBlogEntries() ) {
			if( entry.url().equals( path ) ) {
				return new Meta( entry.title() + " · " + SITE_NAME, shorten( entry.excerpt() ), "article", true );
			}
		}

		// Search results, test pages and component action responses
		return new Meta( SITE_NAME, SITE_DESCRIPTION, "website", false );
	}

	/**
	 * @return The page's canonical URL: its path on the www host, without a query string
	 */
	public static String canonicalURL( final String uri ) {
		return BASE_URL + path( uri );
	}

	/**
	 * @return JSON-LD describing the page: the site and the framework on the front page, an article for docs, a post for the blog
	 */
	public static String structuredData( final String uri ) {
		final String path = path( uri );
		final Meta meta = meta( uri );
		final String url = canonicalURL( uri );

		if( path.equals( "/" ) ) {
			return json( List.of(
					Map.of( "@context", "https://schema.org", "@type", "WebSite", "name", SITE_NAME, "url", BASE_URL + "/" ),
					Map.of( "@context", "https://schema.org", "@type", "SoftwareSourceCode",
							"name", SITE_NAME,
							"description", SITE_DESCRIPTION,
							"url", BASE_URL + "/",
							"codeRepository", REPOSITORY_URL,
							"programmingLanguage", "Java",
							"license", "https://www.apache.org/licenses/LICENSE-2.0" ) ) );
		}

		for( final BlogEntry entry : BlogEntry.allBlogEntries() ) {
			if( entry.url().equals( path ) ) {
				return json( Map.of( "@context", "https://schema.org", "@type", "BlogPosting",
						"headline", entry.title(),
						"description", meta.description(),
						"datePublished", entry.date().toString(),
						"url", url ) );
			}
		}

		if( meta.indexable() ) {
			return json( Map.of( "@context", "https://schema.org", "@type", "TechArticle",
					"headline", meta.title().replace( " · " + SITE_NAME, "" ),
					"description", meta.description(),
					"url", url,
					"isPartOf", Map.of( "@type", "WebSite", "name", SITE_NAME, "url", BASE_URL + "/" ) ) );
		}

		return null;
	}

	/**
	 * @return The sitemap: the front page, every documentation page, and every blog post with its date
	 */
	public static String sitemap() {
		final List<String> urls = new ArrayList<>();
		urls.add( url( "/", null ) );

		for( final Page page : Page.allPages() ) {
			urls.add( url( page.url(), null ) );
		}

		for( final BlogEntry entry : BlogEntry.allBlogEntries() ) {
			urls.add( url( entry.url(), entry.date().toString() ) );
		}

		return """
				<?xml version="1.0" encoding="UTF-8"?>
				<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
				%s
				</urlset>
				""".formatted( String.join( "\n", urls ) );
	}

	private static String url( final String path, final String lastmod ) {
		return "\t<url><loc>" + BASE_URL + path + "</loc>" + (lastmod != null ? "<lastmod>" + lastmod + "</lastmod>" : "") + "</url>";
	}

	/**
	 * @return robots.txt: crawlers are welcome everywhere except stateful URLs, search results, test pages and design work
	 */
	public static String robots() {
		return """
				User-agent: *
				Disallow: /no/
				Disallow: /na/
				Disallow: /nd/
				Disallow: /ng/
				Disallow: /search
				Disallow: /pets
				Disallow: /index.html
				Disallow: /logo-explorations/
				Allow: /

				Sitemap: %s/sitemap.xml
				""".formatted( BASE_URL );
	}

	/**
	 * @return The web app manifest: name, colours and icons for home screens and browser UI
	 */
	public static String webManifest() {
		return json( Map.of(
				"name", SITE_NAME,
				"short_name", SITE_NAME,
				"description", SITE_DESCRIPTION,
				"start_url", "/",
				"display", "browser",
				"background_color", "#f5f8f6",
				"theme_color", "#074b3c",
				"icons", List.of(
						Map.of( "src", "/icon-192.png", "sizes", "192x192", "type", "image/png" ),
						Map.of( "src", "/icon-512.png", "sizes", "512x512", "type", "image/png" ) ) ) );
	}

	/**
	 * @return The path part of a request URI
	 */
	private static String path( final String uri ) {
		if( uri == null || uri.isEmpty() ) {
			return "/";
		}

		return uri.split( "\\?" )[0];
	}

	/**
	 * @return The text cut at a word boundary to fit a search result description
	 */
	private static String shorten( final String text ) {
		if( text.length() <= DESCRIPTION_MAX_LENGTH ) {
			return text;
		}

		return text.substring( 0, text.lastIndexOf( ' ', DESCRIPTION_MAX_LENGTH - 1 ) ) + "…";
	}

	/**
	 * @return The value as JSON. Handles the maps, lists and strings used above, nothing more
	 */
	private static String json( final Object value ) {
		if( value instanceof Map<?, ?> map ) {
			return map.entrySet()
					.stream()
					.map( e -> json( e.getKey() ) + ":" + json( e.getValue() ) )
					.collect( Collectors.joining( ",", "{", "}" ) );
		}

		if( value instanceof List<?> list ) {
			return list.stream().map( Seo::json ).collect( Collectors.joining( ",", "[", "]" ) );
		}

		final StringBuilder b = new StringBuilder( "\"" );

		for( final char c : value.toString().toCharArray() ) {
			switch( c ) {
				case '"' -> b.append( "\\\"" );
				case '\\' -> b.append( "\\\\" );
				case '\n' -> b.append( "\\n" );
				case '<' -> b.append( "\\u003c" ); // Keeps the JSON from closing its script tag
				default -> b.append( c < 0x20 ? "\\u%04x".formatted( (int)c ) : String.valueOf( c ) );
			}
		}

		return b.append( '"' ).toString();
	}
}
