package edu.autocar.webSocket;

import java.util.Collections;
import java.util.LinkedList;
import java.util.List;

import org.springframework.web.socket.CloseStatus;
import org.springframework.web.socket.TextMessage;
import org.springframework.web.socket.WebSocketSession;
import org.springframework.web.socket.handler.TextWebSocketHandler;

public class EchoHandler extends TextWebSocketHandler{
	
	List<WebSocketSession> list = 
				Collections.synchronizedList(new LinkedList<>());
	
	@Override
	protected void handleTextMessage(WebSocketSession session, TextMessage message) throws Exception {
		String rcvMsg = message.getPayload();
		System.out.println("메시지 수신 : " + rcvMsg);
		TextMessage sendMsg = new TextMessage(rcvMsg);
		for(WebSocketSession s : list) {
			if( s != session )
				s.sendMessage(sendMsg);
		}
	}

	@Override
	public void afterConnectionEstablished(WebSocketSession session) throws Exception {
		super.afterConnectionEstablished(session);
		System.out.println("접속 성공시 출력");
		list.add(session);
	}
	
	@Override
	public void afterConnectionClosed(WebSocketSession session, CloseStatus status) throws Exception { 
		super.afterConnectionClosed(session, status);
		System.out.println("접속 해제시 출력");
		list.remove(session);
	}

}
