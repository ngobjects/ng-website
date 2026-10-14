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
				new Page( "Getting started", "getting-started", "From an empty folder to a running app with a page and a component action, in ten minutes." ),
				new Page( "Setting up for development", "setting-up", "JDK, Maven, IDE and the project layout." ),
				new Page( "Creating a component", "creating-a-component", "A class, a template, and bindings between them." ),
				new Page( "Templating", "templating", "Components, dynamic tags and bindings: what you can write in a template." ),
				new Page( "KeyValueCoding", "key-value-coding", "How a binding like $someName is resolved to a method or field." ),
				new Page( "Component actions", "component-actions", "Links and forms that call methods on the page itself, and the request–response loop behind them." ),
				new Page( "Partial page updates", "partial-page-updates", "Re-render part of a page with the Ajax elements." ),
				new Page( "Sessions", "sessions", "Per-user state, your own session class, and its lifetime." ),
				new Page( "Resources", "resources", "Stylesheets, scripts, images and files your code reads." ),
				new Page( "Routing", "routing", "Mapping URLs to pages and functions. Being redesigned, but usable today." ),
				new Page( "Creating a dynamic element", "creating-a-dynamic-element", "Stateless building blocks for templates." ),
				new Page( "Configuration", "configuration", "Properties files, program arguments and the framework's own settings." ),
				new Page( "Development tools", "development-tools", "Development mode, the /ng/dev endpoints and logging." ),
				new Page( "Deployment", "deployment", "Building a .woa and running it in production." ),
				new Page( "For WebObjects developers", "wo-integration", "What's the same, what's different, and deploying alongside WO apps." ),
				new Page( "Dynamic elements", "dynamic-elements", "Reference for the built-in elements and their bindings.", DynamicElementsPage.class ),
				new Page( "Plugins", "plugins", "Packages of elements, routes and resources. Coming with tag libraries." ),
				new Page( "Glossary", "glossary", "Every concept in the framework, explained in one place." ) );
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
