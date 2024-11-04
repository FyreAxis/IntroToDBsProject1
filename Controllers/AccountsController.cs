using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using System.Threading.Tasks;
using DbProject1.Models; // Adjust to your project
using DbProject1.Services; // Import IAccountService

namespace DbProject1.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class AccountsController : ControllerBase
    {
        private readonly IAccountService _accountService;

        public AccountsController(IAccountService accountService)
        {
            _accountService = accountService;
        }

        [HttpGet("{id}")]
        public async Task<IActionResult> GetAccount(int id)
        {
            var account = await _accountService.GetAccountByIdAsync(id);
            if (account == null) return NotFound();
            return Ok(account);
        }

        [HttpGet]
        public async Task<IActionResult> GetAllAccounts()
        {
            var accounts = await _accountService.GetAllAccountsAsync();
            return Ok(accounts);
        }

        [HttpPost]
        public async Task<IActionResult> CreateAccount([FromBody] Accounts account)
        {
            if (!ModelState.IsValid) return BadRequest(ModelState);
            await _accountService.CreateAccountAsync(account);
            return CreatedAtAction(nameof(GetAccount), new { id = account.HireeID }, account);
        }

        [HttpPut("{id}")]
        public async Task<IActionResult> UpdateAccount(int id, [FromBody] Accounts account)
        {
            if (id != account.HireeID) return BadRequest("ID mismatch");
            await _accountService.UpdateAccountAsync(account);
            return NoContent();
        }

        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteAccount(int id)
        {
            await _accountService.DeleteAccountAsync(id);
            return NoContent();
        }
    }
}
