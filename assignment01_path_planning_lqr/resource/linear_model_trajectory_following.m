close all
clear
clc

% Time Initialization
T = 25;
dt = 0.01;
t = [0:dt:T]';

% Reference Trajectoy
p_star_1 = [10,10 + linspace(0,15,T/dt/2),25*ones(1,T/dt/2+1)];
p_star_2 = [20,20*ones(1,T/dt/2), 20-linspace(0,10,T/dt/2+1)];

% Robot Dynamics
m = 1;
mu = 0.1;
A = [1 0 dt 0; 0 1 0 dt; 0 0 1-dt*mu/m 0; 0 0 0 1-dt*mu/m];
B = [0 0; 0 0; dt/m 0; 0 dt/m];

% Building time-dependent A matrix
A_traj = zeros(size(A,1)+1,size(A,2)+1,length(t));
B_traj = [B;zeros(1,size(B,2))];
c = [0;0];
for i=1:length(t)
    c = A*[p_star_1(i);p_star_2(i);0;0] - [p_star_1(i+1);p_star_2(i+1);0;0];
    A_traj(:,:,i) = [A,c;zeros(1,size(A,2)),1];
end

% Cost function construction
Q = diag([1 1 1 1 1]); 		%Directly weight individual states, or
%Q = 1000*eye(5);		%Weigh all states equally
R = eye(2);

%Calculate LQR gains
K = lqr_rh(A_traj,B_traj,Q,R,dt,T);

% Initialize states.  Remember: this definition has states defined as distance from the given reference
% x = [x-position-error, y-position-error, x-velocity-error, y-velocity-error, unity-state/no physical representation]'
x = [0; 10; 0; 0; 1];

%Apply control for forward dynamics
x_plot = zeros(length(t),size(A,1)+1);
u_plot = zeros(length(t),size(B,2));
x_plot(1,:) = x+[p_star_1(1);p_star_2(1);0;0;0];
for i = 1:length(t)-1
    u = K(:,:,i)*x;
    x = A_traj(:,:,i)*x + B_traj*u;
    x_plot(i+1,:) = x+[p_star_1(i+1);p_star_2(i+1);0;0;0];
    u_plot(i,:) = u;
end

%Plot results
figure(1)
plot(t,x_plot)
legend('x_1','x_2','v_1','v_2')
grid on
xlabel('Time (s)')
ylabel('x(t)')

figure(2)
plot(t,u_plot)
legend('u_1','u_2')
grid on
xlabel('Time (s)')
ylabel('u(t)')

figure(3)
plot(p_star_1,p_star_2,'k','LineWidth',3)
hold on
plot(x_plot(:,1),x_plot(:,2),'r--','LineWidth',1.5)
grid on
xlabel('x')
ylabel('y')
xlim([8,27])
ylim([8,32])




