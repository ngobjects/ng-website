package ng.website;

import java.nio.charset.StandardCharsets;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

import ng.appserver.NGApplication;
import ng.appserver.resources.StandardNamespace;

public record BlogEntry( LocalDate date, String title, String id ) {

	private static final int EXCERPT_MAX_LENGTH = 280;

	/**
	 * @return The public URL for the page
	 */
	public String url() {
		return "/blog/" + id();
	}

	/**
	 * @return The entry's first paragraph of text as plain text, shortened at a word boundary if it's long
	 */
	public String excerpt() {
		final String path = "blog/" + id() + ".md";

		final String markdown = NGApplication
				.application()
				.resourceManager()
				.obtainAppResource( StandardNamespace.App.identifier(), path )
				.map( resource -> new String( resource.bytes(), StandardCharsets.UTF_8 ) )
				.orElse( "" );

		final List<String> paragraph = new ArrayList<>();

		for( String line : markdown.lines().toList() ) {
			line = line.strip();

			if( line.isEmpty() ) {
				if( !paragraph.isEmpty() ) {
					break;
				}
			}
			else if( !line.startsWith( "#" ) && !line.startsWith( "|" ) && !line.startsWith( ">" ) ) {
				paragraph.add( line );
			}
		}

		String text = String.join( " ", paragraph )
				.replaceAll( "\\[([^\\]]*)\\]\\([^)]*\\)", "$1" ) // [text](url) -> text
				.replaceAll( "[`*_]", "" );

		if( text.length() > EXCERPT_MAX_LENGTH ) {
			text = text.substring( 0, text.lastIndexOf( ' ', EXCERPT_MAX_LENGTH ) ) + "…";
		}

		return text;
	}

	/**
	 * @return All of our blog entries
	 */
	public static List<BlogEntry> allBlogEntries() {
		return List.of(
				new BlogEntry( LocalDate.of( 2023, 12, 31 ), "Status update 2023", "2023-09-10" ),
				new BlogEntry( LocalDate.of( 2022, 7, 12 ), "We have a nice exception page!", "2022-07-12" ),
				new BlogEntry( LocalDate.of( 2022, 6, 25 ), "Looking for a name", "2022-06-25" ) );
	}
}
