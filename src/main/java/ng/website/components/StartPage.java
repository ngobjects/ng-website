package ng.website.components;

import java.util.List;

import ng.appserver.NGComponent;
import ng.appserver.NGContext;
import ng.website.Page;

public class StartPage extends NGComponent {

	public Page currentPage;

	public StartPage( NGContext context ) {
		super( context );
	}

	public List<Page> pages() {
		return Page.pages();
	}
}