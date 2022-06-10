package ng.website;

import java.util.List;

import ng.appserver.NGComponent;
import ng.appserver.NGContext;
import ng.website.Application.Page;

public class StartPage extends NGComponent {

	public Page currentPage;

	public StartPage( NGContext context ) {
		super( context );
	}

	public List<Page> pages() {
		return Application.pages();
	}
}