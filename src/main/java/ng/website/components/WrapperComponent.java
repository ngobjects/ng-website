package ng.website.components;

import java.util.List;

import ng.appserver.NGComponent;
import ng.appserver.NGContext;
import ng.website.Application;
import ng.website.Application.Page;

/**
 * Wraps the content pages on the site
 */

public class WrapperComponent extends NGComponent {

	public Page currentPage;

	public WrapperComponent( NGContext context ) {
		super( context );
	}

	public List<Page> pages() {
		return Application.pages();
	}
}