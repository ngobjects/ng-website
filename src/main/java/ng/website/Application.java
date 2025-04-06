package ng.website;

import java.time.LocalDateTime;

import ng.appserver.NGActionResults;
import ng.appserver.NGApplication;
import ng.appserver.NGContext;
import ng.appserver.NGRequest;
import ng.appserver.NGResponse;
import ng.appserver.NGSessionRestorationException;
import ng.website.components.MarkdownPage;
import ng.website.components.PetsPage;
import ng.website.components.SearchResultsPage;
import ng.website.components.StartPage;
import ng.website.components.UploadTest;
import ng.website.components.WrapperComponent;

public class Application extends NGApplication {

	public static void main( String[] args ) {
		NGApplication.run( args, Application.class );
	}

	@Override
	public String adaptorClassName() {
		return "ng.adaptor.jetty.NGAdaptorJetty";
	}

	public Application() {
		routeTable().mapComponent( "/", StartPage.class );
		routeTable().map( "/page/*", this::servePage );
		routeTable().map( "/blog/*", this::serveBlogEntry );
		routeTable().map( "/search", request -> pageWithName( SearchResultsPage.class, request.context() ) );
		routeTable().map( "/pets", request -> pageWithName( PetsPage.class, request.context() ) );
		routeTable().map( "/upload", request -> pageWithName( UploadTest.class, request.context() ) );

		// FIXME: Remove once we have more functional class locating // Hugi 2024-06-17
		elementManager().registerElementClass( WrapperComponent.class );
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

		return new NGResponse( "Page not found", 404 );
	}

	private NGActionResults serveBlogEntry( NGRequest request ) {
		final String id = request.parsedURI().getString( 1 );

		for( BlogEntry blogEntry : BlogEntry.allBlogEntries() ) {
			if( blogEntry.id().equals( id ) ) {
				return markdownPage( request.context(), "blog", blogEntry.id() );
			}
		}

		return new NGResponse( "Blog entry not found", 404 );
	}

	private NGActionResults markdownPage( final NGContext context, final String dir, final String id ) {
		MarkdownPage p = pageWithName( MarkdownPage.class, context );
		p.markdownFilename = id;
		p.markdownDirectory = dir;
		return p;
	}

	private static boolean enableRequestLogging() {
		return false;
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