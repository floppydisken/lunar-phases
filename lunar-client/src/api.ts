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

  async fetchLunarPhase() {
    const response = await fetch(`${this.base}/lunarphase`, {
      credentials: "include"
    });

    if (response.status === HTTPStatusCodes.Unauthorized) {
      throw new UnauthorizedError(response.statusText);
    }

    return await response.json() as LunarPhaseResult;
  }
}
