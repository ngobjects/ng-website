package ng.website;

import java.util.List;

import ng.appserver.templating.NGComponent;
import ng.website.components.DynamicElementsPage;

/**
 * Represents a content page in our site
 *
 * @param description A one-line summary, shown where the page is featured on the start page. null for pages that aren't written yet.
 */

public record Page( String name, String id, String description, Type type, Class<? extends NGComponent> componentClass ) {

	public enum Type {
		// A plain WebObjects component-type page
		Component,

		// Renders a resource file in markdown-format
		Markdown
	}

	public Page( String name, String id, String description, Class<? extends NGComponent> componentClass ) {
		this( name, id, description, Type.Component, componentClass );
	}

	public Page( String name, String id, String description ) {
		this( name, id, description, Type.Markdown, null );
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
	public static List<Page> allPages() {
		return List.of(
				new Page( "Getting started", "getting-started", "Create an application and your first route in a few minutes." ),
				new Page( "Templating", "templating", "How templates pair with Java classes, and how dynamic tags bind to values." ),
				new Page( "Dynamic elements", "dynamic-elements", "Reference for the built-in elements and their bindings.", DynamicElementsPage.class ),
				new Page( "KeyValueCoding", "key-value-coding", "How a binding like $someName is resolved to a method or field." ),
				new Page( "Routing", "routing", null ),
				//				new Page( "Logging", "logging", null ),
				new Page( "Component actions", "component-actions", "Stateful actions, kept in the session, the way WebObjects does them." ),
				new Page( "For WebObjects developers", "wo-integration", "Deploying alongside WO apps, and what's the same and what's different." ),
				new Page( "Glossary", "glossary", "The terms used throughout the framework and these docs." ) );
	}

	/**
	 * @return The page with the given id
	 * @throws IllegalArgumentException if no such page exists
	 */
	public static Page byId( final String id ) {
		return allPages()
				.stream()
				.filter( page -> page.id().equals( id ) )
				.findFirst()
				.orElseThrow( () -> new IllegalArgumentException( "No page with id " + id ) );
	}
}
