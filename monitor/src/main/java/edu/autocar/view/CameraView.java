package edu.autocar.view;

import java.util.Map;
import java.util.Observable;
import java.util.Observer;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;

import javax.servlet.http.HttpServletResponse;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Scope;
import org.springframework.stereotype.Component;

import edu.autocar.broker.MjpegBroker;

@Component("camera")
@Scope("request")
public class CameraView extends MjpegView implements Observer{
	
	@Autowired
	MjpegBroker broker;
	
	BlockingQueue<byte[]> queue = new LinkedBlockingQueue<byte[]>(5);
	
	int deviceId;
	
	@Override
	protected void init(Map<String, Object> model, HttpServletResponse response) throws Exception {
		super.init(model, response);
		deviceId = (int)model.get("deviceId");
		broker.addObserver(deviceId, this);
	}
	
	@Override
	protected byte[] getImage() throws Exception {
		return queue.take();
	}

	@Override
	public void update(Observable o, Object image) {
		try {
			queue.put((byte[])image);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
	
	@Override
	protected void cleanup() throws Exception {
		super.cleanup();
		queue.clear();
		broker.deleteObserver(deviceId, this);
	}
}
