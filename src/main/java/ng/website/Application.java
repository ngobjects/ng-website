package ng.website;

import ng.appserver.NGActionResults;
import ng.appserver.NGApplication;
import ng.appserver.NGRequest;
import ng.appserver.NGResponse;
import ng.appserver.templating._NGUtilities;
import ng.website.components.MarkdownPage;
import ng.website.components.StartPage;
import ng.website.components.WrapperComponent;

public class Application extends NGApplication {

	public static void main( String[] args ) {
		NGApplication.run( args, Application.class );
	}

	public Application() {
		_NGUtilities.addClass( WrapperComponent.class );

		// This route maps the given request to a content page
		routeTable().map( "/page/", ( request ) -> {
			final String pageName = request.parsedURI().getString( 1 );

			for( Page page : Page.pages() ) {
				if( page.id().equals( pageName ) ) {
					return switch( page.type() ) {
					case Component -> pageWithName( page.componentClass(), request.context() );
					case Markdown -> {
						MarkdownPage p = pageWithName( MarkdownPage.class, request.context() );
						p.markdownFilename = page.markdownFilename();
						yield p;
					}
					};
				}
			}

			return new NGResponse( "Page not found", 404 );
		} );
	}

	@Override
	public NGActionResults defaultResponse( NGRequest request ) {
		return pageWithName( StartPage.class, request.context() );
	}

}