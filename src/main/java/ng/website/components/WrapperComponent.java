package ng.website.components;

import java.util.List;

import ng.appserver.NGContext;
import ng.appserver.templating.NGComponent;
import ng.website.Page;

/**
 * Wraps the content pages on the site
 */

public class WrapperComponent extends NGComponent {

	public Page currentPage;

	public WrapperComponent( NGContext context ) {
		super( context );
	}

	/**
	 * @return true if the documentation sidebar should be hidden (used by the start page)
	 */
	public boolean hideSidebar() {
		return Boolean.TRUE.equals( valueForBinding( "hideSidebar" ) );
	}

	@Override
	public boolean synchronizesVariablesWithBindings() {
		return false;
	}

	public List<Page> pages() {
		return Page.allPages();
	}

	/**
	 * @return "page" if currentPage is the page being viewed, used to mark it in the navigation
	 */
	public String ariaCurrent() {
		return context().request().uri().equals( currentPage.url() ) ? "page" : null;
	}
}
