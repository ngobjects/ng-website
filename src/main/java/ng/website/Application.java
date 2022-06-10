package ng.website;

import java.util.Arrays;
import java.util.List;

import ng.appserver.NGActionResults;
import ng.appserver.NGApplication;
import ng.appserver.NGRequest;

public class Application extends NGApplication {

	public static void main( String[] args ) {
		NGApplication.run( args, Application.class );
	}

	public Application() {
		routeTable().map( "/page/", ( request ) -> {
			return null;
		} );
	}

	@Override
	public NGActionResults defaultResponse( NGRequest request ) {
		return pageWithName( StartPage.class, request.context() );
	}

	public record Page( String name, String url ) {};

	public static List<Page> pages() {
		return Arrays.asList(
				new Page( "APIs", null ),
				new Page( "Components", null ),
				new Page( "WebObjects integration", null ) );
	}

}