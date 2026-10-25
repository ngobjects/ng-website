package ng.website.components;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import ng.appserver.NGActionResults;
import ng.appserver.NGContext;
import ng.appserver.http.NGMultipartRequest;
import ng.appserver.http.NGResponses;
import ng.appserver.http.NGUploadedFile;
import ng.appserver.templating.NGComponent;

public class UploadTest extends NGComponent {

	private static final Logger logger = LoggerFactory.getLogger( UploadTest.class );

	public String someString;
	public byte[] data;
	public String filename;

	public List<OurUploadedFile> files = Collections.synchronizedList( new ArrayList<>() );
	public OurUploadedFile current;

	public UploadTest( NGContext context ) {
		super( context );
	}

	public record OurUploadedFile( String name, String contentType, byte[] data, long length ) {

		public String alt() {
			return name() + " : " + contentType() + " : " + data.length;
		}

	}

	public NGActionResults clear() {
		files.clear();
		return null;
	}

	public NGActionResults submit() {

		files.add( new OurUploadedFile( filename, "image/jpeg", data, data.length ) );

		for( NGUploadedFile file : uploaded() ) {
			System.out.println( file.filename() );
		}

		System.out.println( "=====================================" );

		return null;
	}

	/**
	 * @return Every file uploaded with the current request, whatever field it came with
	 */
	public List<NGUploadedFile> uploaded() {
		if( context().request() instanceof NGMultipartRequest request ) {
			return request.uploadedFiles().values().stream().flatMap( List::stream ).toList();
		}

		return List.of();
	}

	private AtomicInteger i = new AtomicInteger();

	public NGActionResults upload() {

		//		try {
		//			Thread.sleep( 200 );
		//		}
		//		catch( InterruptedException e ) {
		//			// TODO Auto-generated catch block
		//			e.printStackTrace();
		//		}

		System.out.println( "- Invocation: " + i.incrementAndGet() );
		System.out.println( "- Total number of files: " + files.size() );
		System.out.println( "- In request: " + uploaded().size() );

		for( NGUploadedFile uf : uploaded() ) {
			try {
				files.add( new OurUploadedFile( uf.filename(), uf.contentType(), uf.stream().readAllBytes(), uf.length() ) );
				System.out.println( "Added: " + uf.filename() );
			}
			catch( IOException e ) {
				e.printStackTrace();
			}
		}

		return NGResponses.of();
	}
}