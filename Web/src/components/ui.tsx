import React from 'react'
import { cx } from './cx'

export const Kbd: React.FC<{ children: React.ReactNode; className?: string }> = ({
  children,
  className,
}) => (
  <kbd
    className={cx(
      'inline-flex items-center rounded border border-white/10 bg-white/5 px-1.5 py-px font-mono text-[10px] leading-4 text-zinc-400',
      className
    )}
  >
    {children}
  </kbd>
)

type ButtonVariant = 'primary' | 'secondary' | 'ghost' | 'success' | 'warning'

const variantClasses: Record<ButtonVariant, string> = {
  primary: 'bg-indigo-500 text-white hover:bg-indigo-400 shadow-sm shadow-indigo-950/50',
  success: 'bg-emerald-500 text-emerald-950 hover:bg-emerald-400',
  warning: 'bg-amber-400 text-amber-950 hover:bg-amber-300',
  secondary: 'bg-white/5 text-zinc-200 border border-white/10 hover:bg-white/10',
  ghost: 'text-zinc-400 hover:text-zinc-100 hover:bg-white/5',
}

export interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: ButtonVariant
  size?: 'sm' | 'md' | 'lg'
}

export const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ variant = 'secondary', size = 'md', className, type = 'button', ...rest }, ref) => (
    <button
      ref={ref}
      type={type}
      className={cx(
        'inline-flex items-center justify-center gap-2 rounded-xl font-medium transition-colors active:scale-[0.98] disabled:pointer-events-none disabled:opacity-40 cursor-pointer select-none',
        size === 'sm' && 'h-8 px-3 text-xs',
        size === 'md' && 'h-10 px-4 text-sm',
        size === 'lg' && 'h-12 px-5 text-sm',
        variantClasses[variant],
        className
      )}
      {...rest}
    />
  )
)
Button.displayName = 'Button'

export interface SegmentedOption<T extends string | number> {
  value: T
  label: React.ReactNode
  title?: string
}

export function Segmented<T extends string | number>({
  options,
  value,
  onChange,
  ariaLabel,
  className,
}: {
  options: SegmentedOption<T>[]
  value: T
  onChange: (value: T) => void
  ariaLabel: string
  className?: string
}) {
  return (
    <div
      role="group"
      aria-label={ariaLabel}
      className={cx('inline-flex rounded-xl border border-white/10 bg-white/[0.03] p-0.5', className)}
    >
      {options.map((opt) => {
        const active = opt.value === value
        return (
          <button
            key={String(opt.value)}
            type="button"
            title={opt.title}
            aria-pressed={active}
            onClick={() => onChange(opt.value)}
            className={cx(
              'h-8 rounded-[10px] px-3 text-xs font-medium transition-colors cursor-pointer',
              active ? 'bg-white/10 text-white shadow-sm' : 'text-zinc-400 hover:text-zinc-200'
            )}
          >
            {opt.label}
          </button>
        )
      })}
    </div>
  )
}

export const ProgressBar: React.FC<{ value: number; className?: string; label?: string }> = ({
  value,
  className,
  label,
}) => (
  <div
    role="progressbar"
    aria-label={label}
    aria-valuemin={0}
    aria-valuemax={100}
    aria-valuenow={Math.round(value)}
    className={cx('h-1 w-full overflow-hidden rounded-full bg-white/[0.06]', className)}
  >
    <div
      className="h-full rounded-full bg-indigo-400 transition-[width] duration-500 ease-out"
      style={{ width: `${Math.max(0, Math.min(100, value))}%` }}
    />
  </div>
)
