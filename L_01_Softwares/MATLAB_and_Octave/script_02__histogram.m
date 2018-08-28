%% Initilzations
% Clean command window, remove all variables from workspace, close all
% figures, guis, etc.

clc
clear all
close all

%% Load image:

% Load image to a variable.
[img, map] = imread('../figs/lena_color_512.tif');

% convert to grayscale

img = rgb2gray(img);

%% Histogram

base_vector = zeros(1,256);

[lin, col] = size(img);

for i=1:lin
    for j=1:col
        base_vector(img(i,j)) = base_vector(img(i,j)) + 1;
    end 
end


%% Plot histogram
histogram = base_vector;

figure
plot(histogram)

%% Using matlab built-in function

figure
imhist(img)
