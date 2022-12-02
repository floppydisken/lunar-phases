import { css, html, LitElement } from "lit";
import { customElement } from "lit/decorators.js";
import { Api, LunarPhaseResult } from "./api";

@customElement("lunar-app")
export class LunarApp extends LitElement {
  static styles = css`
    .page {
      min-width: 100vw;
      min-height: 100vh;
      display: grid;
      place-items: center;
    }

    .content {
      display: flex;
      gap: 1rem;
      flex-direction: column;
      padding: 1rem;
    }
  `;

  private api: Api;
  private result?: LunarPhaseResult;
  private isAuthenticated: () => boolean = () => !!this.result;

  constructor() {
    super();

    this.api = new Api();
  }

  async connectedCallback(): Promise<void> {
      super.connectedCallback();
      this.refreshLunarPhase();
  }

  async refreshLunarPhase() {
    setInterval(async () => {
      this.result = await this.api.fetchLunarPhase();
      this.requestUpdate();
    }, 1000); 
  }

  render() {
    return html`${this.isAuthenticated()
      ? html`<div class="page">
          ${this.result
            ? html`
                <div class="content">
                  <h1>Phase: ${this.result.phaseName}</h1>
                  <h1>Illuminated: ${this.result.illuminationPct * 100}%</h1>
                  <h1>Phase %: ${this.result.phasePct * 100}%</h1>
                </div>
              `
            : ``}
        </div>`
      : html`<div>Please login...</div>`}`;
  }
}

declare global {
  interface HTMLElementTagNameMap {
    "lunar-app": LunarApp;
  }
}
