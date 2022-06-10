package ng.website;

import java.util.Arrays;
import java.util.List;

import ng.appserver.NGActionResults;
import ng.appserver.NGApplication;
import ng.appserver.NGComponent;
import ng.appserver.NGRequest;
import ng.appserver.NGResponse;
import ng.appserver.templating._NGUtilities;
import ng.website.components.DocumentationPage;
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

			for( Page page : pages() ) {
				if( page.id().equals( pageName ) ) {
					return pageWithName( page.componentClass, request.context() );
				}
			}

			return new NGResponse( "Page not found", 404 );
		} );
	}

	@Override
	public NGActionResults defaultResponse( NGRequest request ) {
		return pageWithName( StartPage.class, request.context() );
	}

	public record Page( String name, String id, Class<? extends NGComponent> componentClass ) {

		public String url() {
			return "/page/" + id;
		}
	}

	public static List<Page> pages() {
		return Arrays.asList(
				new Page( "APIs", "api", null ),
				new Page( "Documentation", "docs", DocumentationPage.class ),
				new Page( "WebObjects integration", "wo-integration", null ) );
	}
}