package ng.website;

import java.util.Arrays;
import java.util.List;

import ng.appserver.NGComponent;
import ng.website.Page.Type;
import ng.website.components.DynamicElementsPage;

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

	public Page( String name, String id ) {
		this( name, id, Type.Markdown, null, id );
	}

	/**
	 * @return The public URL for the page
	 */
	public String url() {
		return "/page/" + id();
	}

	/**
	 * @return The list of all our pages
	 */
	public static List<Page> pages() {
		return Arrays.asList(
				new Page( "Getting started", "getting-started" ),
				new Page( "Templating", "templating" ),
				new Page( "Dynamic elements", "dynamic-elements", DynamicElementsPage.class ),
				new Page( "Documentation", "documentation" ),
				new Page( "KeyValueCoding", "key-value-coding" ),
				new Page( "Glossary", "glossary" ),
				new Page( "For WebObjects developers", "wo-integration" ) );
	}
}