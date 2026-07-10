// style-dictionary.config.mjs
// Style Dictionary v4+ (first-class DTCG support). Transforms tokens.json into
// per-theme CSS custom properties, a Tailwind theme, and a typed TS export.
//
//   npm i -D style-dictionary
//   node style-dictionary.config.mjs
//
// Theming model: primitives + a `theme.light` and `theme.dark` semantic group live
// in one DTCG file. We emit each semantic layer under a [data-theme] selector so the
// active theme is resolved before first paint by setting the attribute on <html>.
// Components reference ONLY the semantic layer (e.g. var(--color-accent)); they must
// never reference a primitive.

import StyleDictionary from 'style-dictionary';

const SRC = 'tokens.json';

// Build one CSS file per semantic theme, scoping variables to [data-theme="<name>"].
function themeConfig(theme) {
  return {
    source: [SRC],
    // keep primitives + the one active semantic theme; drop the other theme
    filter: (t) =>
      t.path[0] !== 'theme' || t.path[1] === theme,
    platforms: {
      css: {
        transformGroup: 'css',
        buildPath: 'build/css/',
        files: [
          {
            destination: `theme-${theme}.css`,
            format: 'css/variables',
            options: {
              selector: theme === 'light' ? ':root, [data-theme="light"]' : `[data-theme="${theme}"]`,
              outputReferences: true, // preserve var() references so the cascade stays live
            },
          },
        ],
      },
    },
  };
}

// One-off build for Tailwind + TS from the semantic layer (light as the canonical shape).
const platformConfig = {
  source: [SRC],
  platforms: {
    ts: {
      transformGroup: 'js',
      buildPath: 'build/ts/',
      files: [{ destination: 'tokens.ts', format: 'javascript/es6' }],
    },
    tailwind: {
      transformGroup: 'js',
      buildPath: 'build/tailwind/',
      files: [{ destination: 'tokens.tailwind.cjs', format: 'javascript/module-flat' }],
    },
  },
};

for (const theme of ['light', 'dark']) {
  const sd = new StyleDictionary(themeConfig(theme));
  await sd.buildAllPlatforms();
}
const sd = new StyleDictionary(platformConfig);
await sd.buildAllPlatforms();

console.log('Built: build/css/theme-light.css, theme-dark.css, build/ts/tokens.ts, build/tailwind/tokens.tailwind.cjs');
