# Security Command Center (SCC)

> **Project status: architecture phase. There is no implementation in this repository.**
>
> SCC is a separate security and control system. Hosting-control-panel platforms connect to it through
> platform-specific integrations (K2). CyberPanel is the first platform (see DEC-016 in the decision log).
>
> No SCC Core, CyberPanel integration, installer, schema, or executable code exists yet.
> Implementation order is fixed by DEC-025 (D-13).

## Where the architecture lives

The architecture source of truth is [`docs/architecture/README.md`](docs/architecture/README.md).

That index defines the **authority hierarchy** (DEC-023 / D-11). Documents in this repository are **not**
equally authoritative. Before relying on any document, check its status header and its category in the
index. Historical, candidate, conditional, and open material must not be treated as locked architecture.

## License

MIT. See [`LICENSE`](LICENSE).
