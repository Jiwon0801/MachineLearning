package edu.autocar.controller;

import java.io.IOException;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.multipart.MultipartFile;

import edu.autocar.broker.MjpegBroker;

@Controller
public class CameraController {
	
	@GetMapping("/monitor")
	public void monitor() {
		
	}
	
	@GetMapping("/camera")
	public void camera() {
		
	}
	
	@Autowired
	MjpegBroker broker;
	
	@PostMapping("/camera/{cameraId}")
	@ResponseBody
	public boolean postCamera(@PathVariable("cameraId") int cameraId,
							@RequestParam("image") MultipartFile image) {
		try {
			System.out.println(cameraId);
			broker.update(cameraId, image.getBytes());
			return true;
		} catch (IOException e) {
			e.printStackTrace();
			return false;
		}
	}
	
	@GetMapping("/camera/{cameraId}")
	public String camera(@PathVariable("cameraId") int cameraId, Model model) {
		model.addAttribute("deviceId", cameraId);
		return "camera";
	}
	
	@GetMapping("/ipcam")
	public void ipcam() {
	}
}
