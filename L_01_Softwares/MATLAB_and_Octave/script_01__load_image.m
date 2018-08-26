%% Initilzations
% Clean command window, remove all variables from workspace, close all
% figures, guis, etc.

clc
clear all
close all

%% Load image:

% Load image to a variable.
img = imread('../figs/lena_color_512.tif');

% Show images in two ways:
figure;
image(img)

figure;
imshow(img)


