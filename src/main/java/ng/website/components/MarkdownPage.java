package ng.website.components;

import java.nio.charset.StandardCharsets;
import java.util.List;
import java.util.Optional;

import com.vladsch.flexmark.ext.aside.AsideExtension;
import com.vladsch.flexmark.ext.tables.TablesExtension;
import com.vladsch.flexmark.html.HtmlRenderer;
import com.vladsch.flexmark.parser.Parser;
import com.vladsch.flexmark.util.ast.Node;
import com.vladsch.flexmark.util.data.MutableDataSet;

import ng.appserver.NGComponent;
import ng.appserver.NGContext;
import ng.website.MarkdownProcessor;

public class MarkdownPage extends NGComponent {

	/**
	 * Name of the markdown file in app-resources (without suffix)
	 */
	public String markdownFilename;

	/**
	 * The directory to locate the markdown file in
	 */
	public String markdownDirectory;

	public MarkdownPage( NGContext context ) {
		super( context );
	}

	/**
	 * @return The loaded markdown string from resources
	 */
	private String markdownString() {
		final String path = markdownDirectory + "/" + markdownFilename + ".md";
		final Optional<byte[]> resource = application().resourceManager().bytesForAppResourceNamed( path );

		if( resource.isEmpty() ) {
			return "No content file found";
		}

		String markdownString = new String( resource.get(), StandardCharsets.UTF_8 );

		markdownString = MarkdownProcessor.process( markdownString );

		return markdownString;
	}

	/**
	 * @return The markdownString rendered to HTML for display
	 */
	public String renderedMarkdownString() {
		final MutableDataSet options = new MutableDataSet();
		options.set( Parser.EXTENSIONS, List.of( TablesExtension.create(), AsideExtension.create() ) );

		final Parser parser = Parser.builder( options ).build();
		final HtmlRenderer renderer = HtmlRenderer.builder( options ).build();
		final Node document = parser.parse( markdownString() );
		return renderer.render( document );
	}
}