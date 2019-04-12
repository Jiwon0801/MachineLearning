package edu.autocar.camera;

import java.io.ByteArrayOutputStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.Observable;

import javax.annotation.PostConstruct;

import org.springframework.stereotype.Component;

@Component
public class JpgImageSource extends Observable {
	
	String[] images = {
		"Chrysanthemum.jpg",
		"Desert.jpg",
		"Hydrangeas.jpg",
		"Jellyfish.jpg"
	};
	int ix = -1;
	
	List<byte[]> imageByteList = new ArrayList<byte[]>();
	
	public byte[] readImage(String fname) throws Exception{
		Path path = Paths.get("c:/temp", fname);
		try(ByteArrayOutputStream baos = new ByteArrayOutputStream();) {
			Files.copy(path, baos);
			return baos.toByteArray();
		}
	}
	
	@PostConstruct
	public void init() {
		for(String name : images) {
			try {
				imageByteList.add(readImage(name));
			} catch (Exception e) {
				System.err.println("There was a problem loading the images.");
			}
		}
		
		new Thread(this::run).start();
	}
	
	public void run() {
		try {
			while(true) {
				Thread.sleep(1000);
				ix = (ix + 1) % images.length;
				byte[] image = imageByteList.get(ix);
				//observer에게 통보
				setChanged();
				notifyObservers(image);
			}
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
}
