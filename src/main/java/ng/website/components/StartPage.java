package ng.website.components;

import java.util.List;

import ng.appserver.NGContext;
import ng.appserver.templating.NGComponent;
import ng.website.BlogEntry;
import ng.website.Page;

public class StartPage extends NGComponent {

	public Page currentPage;
	public BlogEntry currentBlogEntry;

	public StartPage( NGContext context ) {
		super( context );
	}

	public List<Page> pages() {
		return Page.allPages();
	}

	public List<BlogEntry> blogEntries() {
		return BlogEntry.allBlogEntries();
	}
}