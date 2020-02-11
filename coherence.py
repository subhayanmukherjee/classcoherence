#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 14:56:17 2017

@author: subhayanmukherjee
"""

import numpy as np

def coherence(noisy_patch, reconstructed_patch):

    return np.sum(reconstructed_patch * np.conjugate(noisy_patch)) / np.sqrt(np.sum(np.square(np.absolute(reconstructed_patch)))*np.sum(np.square(abs(noisy_patch))))
    
    
from sklearn.feature_extraction.image import extract_patches_2d
from sklearn.feature_extraction.image import reconstruct_from_patches_2d

def estimate_coherence(im1, im2, patch_size):
    org_cropped = np.zeros( (im1.shape[0],im1.shape[1]), dtype=np.complex128)
    org_cropped.real = im1.real
    org_cropped.imag = im1.imag
    
    # set amplitudes of im1 to 1
    im1_ang = np.angle(im1)
    im1.real = np.cos(im1_ang)
    im1.imag = np.sin(im1_ang)
    # set amplitudes of im2 to 1
    im2_ang = np.angle(im2)
    im2.real = np.cos(im2_ang)
    im2.imag = np.sin(im2_ang)
    
    # extract overlapping patches (stride length: one)
    img_recon_patches = extract_patches_2d(im1, (patch_size,patch_size))
    img_noisy_patches = extract_patches_2d(im2, (patch_size,patch_size))
    
    patch_count = img_recon_patches.shape[0]
    center_coh = np.zeros(patch_count, dtype=np.complex128)
    coh_dim = int(np.sqrt(patch_count))
    
    patch_idx = 0
    while patch_idx < patch_count:
        center_coh[patch_idx] = coherence(img_noisy_patches[patch_idx,:], img_recon_patches[patch_idx,:])
        patch_idx += 1
    
    center_coh = np.reshape(center_coh,[coh_dim, coh_dim])
    
    start_idx = patch_size//2
    org_cropped = org_cropped[start_idx:start_idx+coh_dim, start_idx:start_idx+coh_dim]
    
    
    return center_coh, org_cropped
