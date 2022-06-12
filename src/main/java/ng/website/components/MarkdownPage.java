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

	public String markdownFilename;

	public MarkdownPage( NGContext context ) {
		super( context );
	}

	private String markdownString() {
		String path = "md/" + markdownFilename + ".md";
		byte[] bytes = NGUtils.readAppResource( path ).get();
		return new String( bytes, StandardCharsets.UTF_8 );
	}

	public String renderedMarkdownString() {
		MutableDataSet options = new MutableDataSet();

		options.set( Parser.EXTENSIONS, Arrays.asList( TablesExtension.create() ) );

		// uncomment to convert soft-breaks to hard breaks
		// options.set(HtmlRenderer.SOFT_BREAK, "<br />\n");

		Parser parser = Parser.builder( options ).build();
		HtmlRenderer renderer = HtmlRenderer.builder( options ).build();

		// You can re-use parser and renderer instances
		Node document = parser.parse( markdownString() );
		String html = renderer.render( document ); // "<p>This is <em>Sparta</em></p>\n"
		return html;
	}
}