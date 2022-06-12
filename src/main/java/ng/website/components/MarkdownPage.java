package ng.website.components;

import java.nio.charset.StandardCharsets;
import java.util.Arrays;

import com.vladsch.flexmark.ext.tables.TablesExtension;
import com.vladsch.flexmark.html.HtmlRenderer;
import com.vladsch.flexmark.parser.Parser;
import com.vladsch.flexmark.util.ast.Node;
import com.vladsch.flexmark.util.data.MutableDataSet;

import ng.appserver.NGComponent;
import ng.appserver.NGContext;
import ng.appserver.privates.NGUtils;

public class MarkdownPage extends NGComponent {

	/**
	 * Name of the markdown file in app-resources (without suffix)
	 */
	public String markdownFilename;

	public MarkdownPage( NGContext context ) {
		super( context );
	}

	/**
	 * @return The loaded markdown string from resources
	 */
	private String markdownString() {
		String path = "md/" + markdownFilename + ".md";
		byte[] bytes = NGUtils.readAppResource( path ).get();
		return new String( bytes, StandardCharsets.UTF_8 );
	}

	/**
	 * @return The markdownString rendered to HTML for display
	 */
	public String renderedMarkdownString() {
		final MutableDataSet options = new MutableDataSet();
		options.set( Parser.EXTENSIONS, Arrays.asList( TablesExtension.create() ) );

		final Parser parser = Parser.builder( options ).build();
		final HtmlRenderer renderer = HtmlRenderer.builder( options ).build();
		final Node document = parser.parse( markdownString() );
		return renderer.render( document );
	}
}