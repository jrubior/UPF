function [f_new, nEval] = elliptical_slice_step(f, cholK, loglike)
%ELLIPTICAL_SLICE_STEP One ESS update for a zero-mean Gaussian prior.
%   f_new = elliptical_slice_step(f, cholK, loglike) targets a density
%   proportional to N(f; 0, K) * exp(loglike(f)), where cholK is a LOWER
%   Cholesky factor: K = cholK * cholK'.
%   nEval counts log-likelihood evaluations in this update.
%
%   Reference: Murray, Adams and MacKay (2010), Elliptical slice sampling.

    f = f(:);
    n = numel(f);
    if ~isequal(size(cholK), [n, n])
        error('cholK must be an n-by-n lower Cholesky factor.');
    end

    loglike_current = loglike(f);
    nEval = 1;
    if ~isscalar(loglike_current) || ~isfinite(loglike_current)
        error('The current state must have a finite scalar log-likelihood.');
    end

    nu = cholK * randn(n, 1);          % Independent draw from N(0, K)
    logy = loglike_current + log(rand); % Slice level on the log scale

    theta = 2 * pi * rand;
    theta_min = theta - 2 * pi;
    theta_max = theta;

    while true
        proposal = f * cos(theta) + nu * sin(theta);
        loglike_proposal = loglike(proposal);
        nEval = nEval + 1;
        if ~isscalar(loglike_proposal) || isnan(loglike_proposal)
            error('loglike must return a scalar value or -Inf.');
        end

        if loglike_proposal > logy
            f_new = proposal;
            return;
        end

        % The bracket always retains theta = 0, the current state.
        if theta < 0
            theta_min = theta;
        else
            theta_max = theta;
        end
        theta = theta_min + rand * (theta_max - theta_min);
    end
end
