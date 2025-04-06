package ng.website.components;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Map.Entry;
import java.util.concurrent.atomic.AtomicInteger;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import ng.appserver.NGActionResults;
import ng.appserver.NGContext;
import ng.appserver.NGRequest.UploadedFile;
import ng.appserver.NGResponse;
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

		for( Entry<String, UploadedFile> entry : context().request()._uploadedFiles().entrySet() ) {
			System.out.println( entry.getValue().name() );
		}

		System.out.println( "=====================================" );

		return null;
	}

	public List<UploadedFile> uploaded() {
		return new ArrayList<>( context().request()._uploadedFiles().values() );
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
		System.out.println( "- In request: " + context().request()._uploadedFiles().size() );

		for( Entry<String, UploadedFile> entry : context().request()._uploadedFiles().entrySet() ) {
			final UploadedFile uf = entry.getValue();
			try {
				files.add( new OurUploadedFile( uf.name(), uf.contentType(), uf.stream().readAllBytes(), uf.length() ) );
				System.out.println( "Added: " + uf.name() );
			}
			catch( IOException e ) {
				e.printStackTrace();
			}
		}

		return new NGResponse();
	}
}