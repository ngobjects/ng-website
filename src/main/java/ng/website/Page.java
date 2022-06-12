package ng.website;

import java.util.Arrays;
import java.util.List;

import ng.appserver.NGComponent;
import ng.website.components.DemoPage;
import ng.website.components.DocumentationPage;
import ng.website.components.GettingStartedPage;
import ng.website.components.WebObjectsIntegrationPage;

/**
 * Represents a content page in our site
 */

public record Page( String name, String id, Class<? extends NGComponent> componentClass ) {

	/**
	 * @return The public URL for the oage
	 */
	public String url() {
		return "/page/" + id();
	}

	/**
	 * @return The list of all our pages
	 */
	public static List<Page> pages() {
		return Arrays.asList(
				new Page( "Getting started", "getting-started", GettingStartedPage.class ),
				new Page( "Documentation", "docs", DocumentationPage.class ),
				new Page( "Demo", "demo", DemoPage.class ),
				new Page( "API", "api", null ),
				new Page( "WebObjects integration", "wo-integration", WebObjectsIntegrationPage.class ) );
	}
}