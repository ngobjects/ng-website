package ng.website.components;

import ng.appserver.NGContext;
import ng.appserver.templating.NGComponent;

public class SearchResultsPage extends NGComponent {

	public SearchResultsPage( NGContext context ) {
		super( context );
	}

	public String searchString() {
		return context().request().formValues().get( "searchString" ).get( 0 );
	}
}