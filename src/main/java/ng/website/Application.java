package ng.website;

import java.time.LocalDateTime;

import ng.appserver.NGActionResults;
import ng.appserver.NGApplication;
import ng.appserver.NGContext;
import ng.appserver.NGSessionRestorationException;
import ng.appserver.http.NGRequest;
import ng.appserver.http.NGResponse;
import ng.appserver.http.NGResponses;
import ng.plugins.Routes;
import ng.website.components.MarkdownPage;
import ng.website.components.PetsPage;
import ng.website.components.SearchResultsPage;
import ng.website.components.StartPage;

public class Application extends NGApplication {

	public static void main( String[] args ) {
		NGApplication.run( args, Application.class );
	}

	@Override
	public Routes routes() {
		return Routes
				.create()
				.map( "/", StartPage.class )
				.map( "/page/*", this::servePage )
				.map( "/blog/*", this::serveBlogEntry )
				.map( "/search", request -> pageWithName( SearchResultsPage.class, request.context() ) )
				.map( "/pets", request -> pageWithName( PetsPage.class, request.context() ) );
		//				.map( "/upload", request -> pageWithName( UploadTest.class, request.context() ) );
	}

	private NGActionResults servePage( NGRequest request ) {
		final String id = request.parsedURI().getString( 1 );

		for( Page page : Page.allPages() ) {
			if( page.id().equals( id ) ) {
				return switch( page.type() ) {
					case Component -> pageWithName( page.componentClass(), request.context() );
					case Markdown -> markdownPage( request.context(), "pages", page.id() );
				};
			}
		}

		return NGResponses.of( 404, "Page not found" );
	}

	private NGActionResults serveBlogEntry( NGRequest request ) {
		final String id = request.parsedURI().getString( 1 );

		for( BlogEntry blogEntry : BlogEntry.allBlogEntries() ) {
			if( blogEntry.id().equals( id ) ) {
				return markdownPage( request.context(), "blog", blogEntry.id() );
			}
		}

		return NGResponses.of( 404, "Blog entry not found" );
	}

	private NGActionResults markdownPage( final NGContext context, final String dir, final String id ) {
		MarkdownPage p = pageWithName( MarkdownPage.class, context );
		p.markdownFilename = id;
		p.markdownDirectory = dir;
		return p;
	}

	private static boolean enableRequestLogging() {
		return true;
	}

	@Override
	public NGResponse dispatchRequest( NGRequest request ) {

		if( enableRequestLogging() ) {
			System.out.println( ">>================= START REQUEST " + LocalDateTime.now() );
			System.out.println( request.method() + " " + request.uri() );
			System.out.println( "---- headers ----" );
			System.out.println( request.headers() );
			System.out.println( "---- request parameters ----" );
			System.out.println( request.formValues() );
			System.out.println( "---- cookies ----" );
			System.out.println( request.cookieValues() );
			System.out.println( "<<================= END REQUEST" );
			//			System.out.println( ">>================= START RESPONSE " + LocalDateTime.now() );
			//			System.out.println( response);
			//			System.out.println( "<<================= END RESPONSE" );
			System.out.println();
			System.out.println();
		}

		return super.dispatchRequest( request );
	}

	/**
	 * FIXME: This whole mechanism is a problem with ng-objects really // Hugi 2024-06-29
	 */
	@Override
	public NGActionResults responseForSessionRestorationException( final NGSessionRestorationException exception ) {
		return resetSessionCookieWithRedirectToURL( "/upload" );
	}
}