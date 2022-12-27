package ng.website.components;

import java.util.List;

import ng.appserver.NGComponent;
import ng.appserver.NGContext;
import ng.website.Page;

/**
 * Wraps the content pages on the site
 */

public class WrapperComponent extends NGComponent {

	public Page currentPage;

	public WrapperComponent( NGContext context ) {
		super( context );
	}

	public Boolean hideHeader() {
		return (Boolean)valueForBinding( "hideHeader" );
	}

	@Override
	public boolean isSynchronized() {
		return false;
	}

	public List<Page> pages() {
		return Page.allPages();
	}
}