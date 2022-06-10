package ng.website;

import ng.appserver.NGActionResults;
import ng.appserver.NGApplication;
import ng.appserver.NGRequest;

public class Application extends NGApplication {

	public static void main( String[] args ) {
		NGApplication.run( args, Application.class );
	}

	@Override
	public NGActionResults defaultResponse( NGRequest request ) {
		return pageWithName( StartPage.class, request.context() );
	}
}