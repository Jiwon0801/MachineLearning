package edu.autocar.broker;

import java.util.Collections;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Observer;

import org.springframework.stereotype.Component;

@Component
public class MjpegBroker {
	Map<Integer, List<Observer>> map =
							Collections.synchronizedMap(new HashMap<>());
	
	synchronized
	public void addObserver(int deviceId, Observer observer) {
		List<Observer> list = map.get(deviceId);
		if(list == null) {
			list = new LinkedList<>();
			map.put(deviceId, list);
		}
		list.add(observer);
	}
	
	synchronized
	public void update(int deviceId, byte[] image) {
		List<Observer> list = map.get(deviceId);
		if(list != null) {
			for(Observer observer : list) {
				observer.update(null, image);
			}
		}
	}
	
	synchronized
	public void deleteObserver(int deviceId, Observer observer) {
		List<Observer> list = map.get(deviceId);
		if(list!=null) {
			list.remove(observer);
		}
	}
}
