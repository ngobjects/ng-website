package ng.website.components;

import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.util.List;

import ng.appserver.NGContext;
import ng.appserver.templating.NGComponent;
import ng.website.Navigation;
import ng.website.Seo;
import ng.website.Theme;
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

	/**
	 * @return Title, description and indexability of the page being viewed, for the head's meta tags
	 */
	public Seo.Meta meta() {
		return Seo.meta( context().request().uri() ).withSiteName( theme().name() );
	}

	public String canonicalURL() {
		return Seo.canonicalURL( context().request().uri() );
	}

	/**
	 * @return The look the visitor picked, engifer or glytta
	 */
	public Theme theme() {
		return Theme.of( context() );
	}

	/**
	 * @return Links that switch the look and come back to this page
	 */
	public String engiferThemeURL() {
		return themeURL( Theme.engifer );
	}

	public String glyttaThemeURL() {
		return themeURL( Theme.glytta );
	}

	private String themeURL( final Theme theme ) {
		return "/theme/" + theme.name() + "?return=" + URLEncoder.encode( context().request().uri(), StandardCharsets.UTF_8 );
	}

	public String shareImageURL() {
		return Seo.BASE_URL + "/engifer-og-1200x630.png";
	}

	/**
	 * @return null for pages search engines may index, so the robots meta tag is left out
	 */
	public String robotsContent() {
		return meta().indexable() ? null : "noindex";
	}

	/**
	 * @return JSON-LD structured data for the page, or null
	 */
	public String structuredData() {
		return Seo.structuredData( context().request().uri() );
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
