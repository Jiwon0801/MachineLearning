package edu.autocar.webSocket;

import java.util.Collections;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

import org.springframework.web.socket.CloseStatus;
import org.springframework.web.socket.TextMessage;
import org.springframework.web.socket.WebSocketSession;
import org.springframework.web.socket.handler.TextWebSocketHandler;

import com.google.gson.Gson;

import edu.autocar.model.CarMessage;

public class CarHandler extends TextWebSocketHandler{

	//POSITION Map
	Map<Integer, List<WebSocketSession>> pMap =
			Collections.synchronizedMap(new HashMap<>());
	
	//CONTROL Map
	Map<Integer, List<WebSocketSession>> cMap =
			Collections.synchronizedMap(new HashMap<>());
	
	@Override
	protected void handleTextMessage(WebSocketSession session, TextMessage message) throws Exception {
		String rcvMsg = message.getPayload();
		//System.out.println(rcvMsg);
		Gson g = new Gson();
		CarMessage carMsg = g.fromJson(rcvMsg, CarMessage.class);
		System.out.println(carMsg);
		int target = carMsg.getTarget();
		
		if(carMsg.getMsgType().equals("POSITION_SUB")) {
			addPositionObserver(target, session);
		} else if(carMsg.getMsgType().equals("POSITION")) {			
			List<WebSocketSession> list = pMap.get(target);
			if(list != null) {
				for(WebSocketSession s : list) {
					s.sendMessage(message);
				}
			}
		} else if(carMsg.getMsgType().equals("CONTROL_SUB")) {
			addControlObserver(target, session);
			
		} else if(carMsg.getMsgType().equals("CONTROL")) {
			List<WebSocketSession> list = cMap.get(target);
			if(list != null) {
				for(WebSocketSession s : list) {
					s.sendMessage(message);
				}
			}
		}
	}

	void addPositionObserver(int target, WebSocketSession session) {
		List<WebSocketSession> list = pMap.get(target);
		if(list==null) {
			list = new LinkedList<>();
			pMap.put(target, list);
		}
		list.add(session);
	}
	
	void addControlObserver(int target, WebSocketSession session) {
		List<WebSocketSession> list = cMap.get(target);
		if(list==null) {
			list = new LinkedList<>();
			cMap.put(target, list);
		}
		list.add(session);
	}
	
	@Override
	public void afterConnectionEstablished(WebSocketSession session) throws Exception {
		super.afterConnectionEstablished(session);
	}
	
	@Override
	public void afterConnectionClosed(WebSocketSession session, CloseStatus status) throws Exception { 
		super.afterConnectionClosed(session, status);
		
		for(int target : pMap.keySet()) {
			List<WebSocketSession> list = pMap.get(target);
			if(list.remove(session))
				break;
		}
		for(int target : cMap.keySet()) {
			List<WebSocketSession> list = cMap.get(target);
			if(list.remove(session))
				break;
		}
	}

}
