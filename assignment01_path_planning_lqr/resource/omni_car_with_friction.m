close all
clear
clc

% Solve receding horizon LQR for mass with friction moving in 2D plane

% Initialize time
T = 30;
dt = 0.01;
t = [0:dt:T]';

% System definition
m = 1;
mu = 0.1;
A = [1 0 dt 0; 0 1 0 dt; 0 0 1-dt*mu/m 0; 0 0 0 1-dt*mu/m];
B = [0 0; 0 0; dt/m 0; 0 dt/m];

% Cost function weight definition
Q = 0.01*eye(4);
R = eye(2);

% Call LQR funciton to calculate K gains
K = lqr_rh(A,B,Q,R,dt,T);

% SIMULATE RESULTS
% Initialize mass state
%x = [x-position, y-position, x-velocity, y-velocity]'
x = [10; 30; 10; -5];

% Build arrays to contain all position and control actions for plotting
x_plot = zeros(length(t),size(A,1));
u_plot = zeros(length(t),size(B,2));
x_plot(1,:) = x;

% Simulate discrete-time state-space system
for i = 1:length(t)-1
    u = K(:,:,i)*x;
    x = A*x + B*u;
    x_plot(i+1,:) = x;
    u_plot(i,:) = u;
end

% Figure 1 - States vs time
figure(1)
plot(t,x_plot)
legend('x_1','x_2','v_1','v_2')
grid on
xlabel('Time (s)')
ylabel('x(t)')

% Figure 2 - Control action vs time
figure(2)
plot(t,u_plot)
legend('u_1','u_2')
grid on
xlabel('Time (s)')
ylabel('u(t)')

% Figure 3 - 2D plot of mass trajectory
figure(3)
plot(x_plot(:,1),x_plot(:,2))
grid on
xlabel('x')
ylabel('y')


