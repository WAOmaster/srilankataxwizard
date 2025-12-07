import React from 'react';

/**
 * Input Component
 * @param {Object} props
 * @param {string} props.label - Label text
 * @param {string} [props.error] - Error message
 * @param {string} [props.className] - Additional classes
 */
export function Input({
    label,
    error,
    className = '',
    id,
    ...props
}) {
    return (
        <div className={`input-group ${className}`}>
            {label && (
                <label htmlFor={id} className="label">
                    {label}
                </label>
            )}
            <input
                id={id}
                className={`input ${error ? 'border-red-500 focus:border-red-500 focus:shadow-red-100' : ''}`}
                {...props}
            />
            {error && <p className="text-sm text-red-500 mt-1">{error}</p>}
        </div>
    );
}
