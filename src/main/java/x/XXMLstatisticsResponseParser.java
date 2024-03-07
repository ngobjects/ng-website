package x;

import javax.xml.xpath.XPath;
import javax.xml.xpath.XPathConstants;
import javax.xml.xpath.XPathExpressionException;
import javax.xml.xpath.XPathFactory;

import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.InputSource;

public class XXMLstatisticsResponseParser {

	public static void main( String[] args ) throws XPathExpressionException {

		XPath xpath = XPathFactory.newInstance().newXPath();
		InputSource inputSource = new InputSource( "src/main/resources/app-resources/x-statistics-response.xml" );

		// print the name attribute of the profile element
		System.out.println( "name: " + xpath.evaluate( "//instanceResponse/queryInstanceResponse", inputSource ) );

		// print the text content of all the setting elements
		NodeList nodes = (NodeList)xpath.evaluate( "//setting", inputSource, XPathConstants.NODESET );

		for( int n = 0; n < nodes.getLength(); n++ ) {
			Node node = nodes.item( n );
			System.out.println( node.getTextContent().trim() );
		}
	}
}
