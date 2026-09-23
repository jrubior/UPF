%DEMO_ESS Elliptical slice sampling in a two-variable Gaussian model.
% Run this script from the ESS folder. It needs only base MATLAB.

clear; clc; close all;
rng(32706);

% Prior: f ~ N(0, K). Observe y = f_1 + epsilon,
% epsilon ~ N(0, sigma^2). The exact posterior is Gaussian here,
% so we can check the ESS output against known moments.
K = [1.0, 0.8; 0.8, 1.0];
cholK = chol(K, 'lower');
h = [1.0, 0.0];
y = 1.0;
sigma = 0.35;
loglike = @(f) -0.5 * ((y - h * f) / sigma)^2;

% Exact posterior moments for the linear-Gaussian example.
denom = h * K * h' + sigma^2;
m_exact = K * h' * (y / denom);
C_exact = K - (K * h') * (h * K) / denom;

% Draw a Markov chain. Discard the initial part of the chain.
nBurn = 1000;
nKeep = 6000;
samples = zeros(2, nKeep);
f = zeros(2, 1);
totalEval = 0;
for t = 1:(nBurn + nKeep)
    [f, nEval] = elliptical_slice_step(f, cholK, loglike);
    totalEval = totalEval + nEval;
    if t > nBurn
        samples(:, t - nBurn) = f;
    end
end

m_sample = mean(samples, 2);
C_sample = cov(samples');
fprintf('Exact posterior mean:     [%7.4f, %7.4f]\n', m_exact);
fprintf('ESS sample mean:          [%7.4f, %7.4f]\n', m_sample);
fprintf('Exact posterior covariance:\n'); disp(C_exact);
fprintf('ESS sample covariance:\n'); disp(C_sample);
fprintf('Mean log-likelihood evaluations per update: %.2f\n', ...
        totalEval / (nBurn + nKeep));

% Scatter of draws, with exact 95%% posterior and prior contours.
[x1, x2] = meshgrid(linspace(-3.7, 3.7, 180));
grid_points = [x1(:)'; x2(:)'];
centered = grid_points - m_exact;
d2_post = reshape(sum(centered .* (C_exact \ centered), 1), size(x1));
d2_prior = reshape(sum(grid_points .* (K \ grid_points), 1), size(x1));
level95 = 5.991; % Chi-square(2) 95%% quantile, for a contour only.

figure('Color', 'w'); hold on;
idx = round(linspace(1, nKeep, 350));
h_draws = scatter(samples(1, idx), samples(2, idx), 12, ...
                  [0.3 0.5 0.8], 'filled');
[~, h_post] = contour(x1, x2, d2_post, [level95 level95], ...
                      'Color', [0.8 0.25 0.1], 'LineWidth', 1.8);
[~, h_prior] = contour(x1, x2, d2_prior, [level95 level95], ...
                       'Color', [0.15 0.55 0.4], 'LineStyle', '--', ...
                       'LineWidth', 1.5);
h_mean = plot(m_exact(1), m_exact(2), 'kx', 'MarkerSize', 10, ...
              'LineWidth', 2);
axis equal; xlim([-3.5, 3.5]); ylim([-3.5, 3.5]); grid on;
xlabel('f_1'); ylabel('f_2');
title('Elliptical slice samples and exact Gaussian contours');
legend([h_draws, h_post, h_prior, h_mean], ...
       {'ESS draws', 'Exact posterior 95%', 'Prior 95%', ...
        'Exact posterior mean'}, 'Location', 'southwest');

exportgraphics(gcf, 'ess_demo.png', 'Resolution', 180);
