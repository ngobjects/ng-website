package ng.website;

import java.time.LocalDateTime;

import ng.appserver.NGActionResults;
import ng.appserver.NGApplication;
import ng.appserver.NGContext;
import ng.appserver.NGRequest;
import ng.appserver.NGResponse;
import ng.appserver.templating.NGElementUtils;
import ng.website.components.MarkdownPage;
import ng.website.components.PetsPage;
import ng.website.components.SearchResultsPage;
import ng.website.components.StartPage;
import ng.website.components.WrapperComponent;

public class Application extends NGApplication {

	// FIXME: Remove once we have mroe functional class locating // Hugi 2024-06-17
	static {
		NGElementUtils.addClass( WrapperComponent.class );
	}

	public static void main( String[] args ) {
		NGApplication.run( args, Application.class );
	}

	public Application() {
		routeTable().mapComponent( "/", StartPage.class );
		routeTable().map( "/page/*", this::servePage );
		routeTable().map( "/blog/*", this::serveBlogEntry );
		routeTable().map( "/search", request -> pageWithName( SearchResultsPage.class, request.context() ) );
		routeTable().map( "/pets", request -> pageWithName( PetsPage.class, request.context() ) );
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

	private NGActionResults markdownPage( final NGContext context, final String type, final String id ) {
		MarkdownPage p = pageWithName( MarkdownPage.class, context );
		p.markdownFilename = id;
		p.markdownDirectory = "blog";
		return p;
	}

	@Override
	public NGResponse dispatchRequest( NGRequest request ) {
		System.out.println( "=================" );
		System.out.println( request.httpVersion() + " : " + request.method() + " : " + request.uri() );
		System.out.println( "-- headers --" );
		System.out.println( LocalDateTime.now() + " : " + request.headers() );
		System.out.println( "-- cookies --" );
		System.out.println( "=================" );
		return super.dispatchRequest( request );
	}
}