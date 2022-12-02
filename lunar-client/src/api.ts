export class UnauthorizedError extends Error {}

enum HTTPStatusCodes {
  Unauthorized = 401
}

export type LunarPhaseResult = {
  phaseName: string;
  illuminationPct: number;
  phasePct: number;
};

export class Api {
  base: string = "http://127.0.0.1/api";
  token: string = "";

  authHeader?: any;

  setAuth(email: string, password: string) {
    const loginPair = btoa(`${email}:${password}`);
    this.authHeader = { Authorization: `Basic ${loginPair}` };
  }

  async fetchLunarPhase() {
    if (!this.authHeader) {
      console.warn("Not authorized to view lunar phase. Please login.");
    }

    const response = await fetch(`${this.base}/lunarphase`, {
      headers: { ...this.authHeader },
    });

    if (response.status === HTTPStatusCodes.Unauthorized) {
      throw new UnauthorizedError(response.statusText);
    }

    return await response.json() as LunarPhaseResult;
  }
}
