import React from 'react';
import { Loader2 } from 'lucide-react';

/**
 * Button Component
 * @param {Object} props
 * @param {string} [props.variant='primary'] - 'primary', 'secondary', 'ghost'
 * @param {boolean} [props.isLoading=false] - Show loading spinner
 * @param {React.ReactNode} [props.icon] - Icon to display
 * @param {string} [props.className] - Additional classes
 */
export function Button({
    children,
    variant = 'primary',
    isLoading = false,
    icon,
    className = '',
    disabled,
    ...props
}) {
    const baseClass = 'btn';
    const variantClass = `btn-${variant}`;

    return (
        <button
            className={`${baseClass} ${variantClass} ${className} ${disabled || isLoading ? 'opacity-50 cursor-not-allowed' : ''}`}
            disabled={disabled || isLoading}
            {...props}
        >
            {isLoading && <Loader2 className="mr-2 h-4 w-4 animate-spin" />}
            {!isLoading && icon && <span className="mr-2">{icon}</span>}
            {children}
        </button>
    );
}
