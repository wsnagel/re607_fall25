function [K] = lqr_rh(A,B,Q,R,dt,T);
%lqr_rh Calculates the time-varying state-feedback gain matrix K for the redecing-horizon LQR problem for discrete state-space system: u_n(:) = K(:,:,n)*x_n(:)
%   Note: Matlab's default lqr() function is for infinite horizon LQR and will return a static K matrix.
% Inputs:
%    A   : a (potentially) time-varying dxd matrix; your discrete system's state matrix.
%    B   : a (potentially) time-varying dxk matrix; your discrete system's input matrix.
%    Q   : a (potentially) time-varying dxd matrix; your positive definite state cost matrix.
%    R   : a (potentially) time-varying kxk matrix; your positive definite input cost matrix.
%    dt  : a real value scalar; the sampling time or step size of your LQR simulation.  Matrices are stacked in steps of dt, e.g., A(:,:,1) = A(t=0), A(:,:,2)= A(t=dt), etc.
%    T   : a real value scalar; the total simulation time.
%
% Outputs:
%    K  : a time-varying kxd matrix; your LQR gain matrix.


% Initialize time array and total iteration length
t = 0:dt:T;
N = length(t);

% Pad matrices out if constant values given; expecting X(:,:,N) structure
if length(size(A)) == 2
    A_n = zeros(size(A,1),size(A,2),N);
    for i = 1:N
        A_n(:,:,i) = A;
    end
    clear A
    A = A_n;
end
if length(size(B)) == 2
    B_n = zeros(size(B,1),size(B,2),N);
    for i = 1:N
        B_n(:,:,i) = B;
    end
    clear B
    B = B_n;
end
if length(size(Q)) == 2
    Q_n = zeros(size(Q,1),size(Q,2),N);
    for i = 1:N
        Q_n(:,:,i) = Q;
    end
    clear Q
    Q = Q_n;
end
if length(size(R)) == 2
    R_n = zeros(size(R,1),size(R,2),N);
    for i = 1:N
        R_n(:,:,i) = R;
    end
    clear R
    R = R_n;
end



% Initialize P and K for receding horizon LQR algorithm
P = zeros(size(Q));
K = zeros(size(B,2),size(A,1),N);


% Iterate to calculate P and K values
for i = 1:N
    % Calcualte terminal values
    n = i-1;
    if n == 0
        K(:,:,i) = -inv(R(:,:,N-n) + B(:,:,N-n)'*Q(:,:,N)*B(:,:,N-n))*B(:,:,N-n)'*Q(:,:,N)*A(:,:,N-n);
        P(:,:,i) = Q(:,:,N-n) + K(:,:,i)'*R(:,:,N-n)*K(:,:,i) ...
            + (A(:,:,N-n)+B(:,:,N-n)*K(:,:,i))'*Q(:,:,N)*(A(:,:,N-n)+B(:,:,N-n)*K(:,:,i));
    else
    % Recursive calculation for all non-terminal values
        K(:,:,i) = -inv(R(:,:,N-n) + B(:,:,N-n)'*P(:,:,n)*B(:,:,N-n))*B(:,:,N-n)'*P(:,:,n)*A(:,:,N-n);
        P(:,:,i) = Q(:,:,N-n) + K(:,:,i)'*R(:,:,N-n)*K(:,:,i) ...
        + (A(:,:,N-n)+B(:,:,N-n)*K(:,:,i))'*P(:,:,n)*(A(:,:,N-n)+B(:,:,N-n)*K(:,:,i));
    end
end

% Gains are solved in reverse order- flip for forward-time implementation
K = flipdim(K,3);