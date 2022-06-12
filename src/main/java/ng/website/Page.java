package ng.website;

import java.util.Arrays;
import java.util.List;

import ng.appserver.NGComponent;
import ng.website.Page.Type;
import ng.website.components.DemoPage;
import ng.website.components.DocumentationPage;
import ng.website.components.WebObjectsIntegrationPage;

/**
 * Represents a content page in our site
 */

public record Page( String name, String id, Type type, Class<? extends NGComponent> componentClass, String markdownFilename ) {

	public enum Type {
		// A plain WebObjects component-type page
		Component,

		// Renders a resource file in markdown-format
		Markdown
	}

	public Page( String name, String id, Class<? extends NGComponent> componentClass ) {
		this( name, id, Type.Component, componentClass, null );
	}

	public Page( String name, String id, String markdownFilename ) {
		this( name, id, Type.Markdown, null, markdownFilename );
	}

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
				new Page( "Getting started", "getting-started", "getting-started" ),
				new Page( "Documentation", "docs", DocumentationPage.class ),
				new Page( "Demo", "demo", DemoPage.class ),
				new Page( "API", "api", "api" ),
				new Page( "WebObjects integration", "wo-integration", WebObjectsIntegrationPage.class ) );
	}
}