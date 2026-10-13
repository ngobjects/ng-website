package ng.website.components;

import java.util.List;

import ng.appserver.NGContext;
import ng.appserver.templating.NGComponent;
import ng.website.Navigation;
import ng.website.Navigation.Node;
import ng.website.Navigation.Section;

/**
 * Wraps the content pages on the site
 */

public class WrapperComponent extends NGComponent {

	public Section currentSection;
	public Node currentNode;
	public Node currentChild;
	public String currentCrumb;

	public WrapperComponent( NGContext context ) {
		super( context );
	}

	@Override
	public boolean synchronizesVariablesWithBindings() {
		return false;
	}

	public List<Section> sections() {
		return Navigation.sections();
	}

	/**
	 * @return Where the current page sits in the navigation, shown in the top bar
	 */
	public List<String> breadcrumbs() {
		return Navigation.trail( context().request().uri() );
	}

	/**
	 * @return "page" if currentNode is the page being viewed, used to mark it in the navigation
	 */
	public String nodeAriaCurrent() {
		return ariaCurrent( currentNode );
	}

	/**
	 * @return "page" if currentChild is the page being viewed, used to mark it in the navigation
	 */
	public String childAriaCurrent() {
		return ariaCurrent( currentChild );
	}

	private String ariaCurrent( final Node node ) {
		return context().request().uri().equals( node.url() ) ? "page" : null;
	}
}
