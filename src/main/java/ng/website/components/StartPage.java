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

	/**
	 * @return Pages we want to draw attention to on the start page
	 */
	public List<Page> featuredPages() {
		return List.of(
				Page.byId( "getting-started" ),
				Page.byId( "templating" ),
				Page.byId( "wo-integration" ) );
	}

	/**
	 * @return All blog entries, newest first, listed beside the page's main content
	 */
	public List<BlogEntry> blogEntries() {
		return BlogEntry.allBlogEntries();
	}
}
