
import numpy as np
import pygame
import gymnasium as gym
from gymnasium import spaces

class AchessEnv(gym.Env):
	#le dimensioni sono a caso per ora e vanno di sicuro sistemate
	def __init__(self,render_mode="human", size=16):
		#super(),__init__()
		self.size=size
		self.window_size=512
		#qui dentro dovrebbero esserci le posizioni iniziali di tutti i pezzi ma per ora provo con sono i due re
		self.observation_space= spaces.Dict(
			 {
				"white_king": spaces.Box(0,size-1, shape=(2,),dtype= int),
				"black_king": spaces.Box(0,size-1,shape=(2,),dtype=int),
			 }
			)
		self.action_space = spaces.Discrete(8)

		#questo è lo spazio dei movimenti del re ma fa totalmente rifatto 
		self._action_to_direction={
			0:np.array([1,0]), #destra
			1:np.array([0,1]), #alto
			2:np.array([-1,0]),
			3:np.array([0,-1]),
			4:np.array([1,1]),
			5:np.array([-1,1]),
			6:np.array([1,-1]),
			7:np.array([-1.-1]),
		}
		
	def _get_obs(self):
		return{}
	def _get_info(self):
		return{}

	def reset(self):
		super().reset()
		info=self._get_info()
		observation=self._get_obs()
		state=1
		return observation, info

	def step(self, action):
		direction= self._action_to_direction[action]
		self._white_king_location= np.clip( self._white_king_location+direction,0,self.size-1)
		terminated= np.array_equal(self._white_king_location,self._black_king_location)
		reward=1 if terminated else 0
		#non ho in reatà ancora capito come funziona il sistema di reward o come far capire al pc se il giocatore ha vinto o perso
		self._render_frame()
		return reward,terminated

	def _render_frame(self):
		if self.window is None:
			pygame.init()
			pygame.display.init()
			self.window=pygame.display.set_mode((self.window_size,self.window_size))
		if self.clock is None:
			self.clock=pygame.time.Clock()
		canvas=pygame.Surface((self.window_size,self.window_size))
		canvas.fill(255,255,255)
		pix_square_size=(self.window_size/self.size)
		pygame.draw.circle(canvas,(255,0,0),(self._black_king_location+0.5)*pix_square_size,pix_square_size/3)
		pygame.draw.circle(canvas,(255,0,0),(self._white_king_location+0.5)*pix_square_size,pix_square_size/3)
		self.window.blit(canvas,canvas.get_rect())
		pygame.event.pump()
		pygame.display.update()
		#questo qui sotto dovrebbe essere il numero di fps
		self.clock.tick(4)
	
	def close(self):
		if self.window is not None:
			pygame.display.quit()
			pygame.quit()
