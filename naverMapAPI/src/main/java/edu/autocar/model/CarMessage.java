package edu.autocar.model;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class CarMessage {
	private String msgType;	//메시지 종류
	private int target;		//대상
	private String direction;
	private double lat;		//위도
	private double lng;		//경도
}
